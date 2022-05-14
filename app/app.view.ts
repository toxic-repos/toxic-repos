namespace $.$$ {
	
	const Data = $mol_data_array(
		$mol_data_record({
			id: $mol_data_integer,
			datetime: $mol_data_string,
			problem_type: $mol_data_string,
			name: $mol_data_string,
			commit_link: $mol_data_string,
			description: $mol_data_string,
		})
	)
	
	export class $toxic_app extends $.$toxic_app {
		
		@ $mol_mem_key
		issues_page_title( id: string ) {
			return this.type_name()[ id ] ?? id
		}
		
		@ $mol_mem
		data_all() {
			const json = this.$.$mol_fetch.json( 'toxic/data/json/toxic-repos.json' )
			return Data( json )
		}
		
		@ $mol_mem
		data_sorted() {
			return this.data_all().slice().sort( $mol_compare_text( item => item.datetime ) ).reverse()
		}
		
		@ $mol_mem
		search( next?: string ) {
			return this.$.$mol_state_arg.value( 'search', next ) ?? ''
		}
		
		@ $mol_mem
		data_filtered() {
			
			let data = this.data_sorted()
			
			const type = this.spread()
			if( type ) data = data.filter( item => item.problem_type === type )
			
			const search = this.search()
			if( search ) data = data.filter(
				$mol_match_text( search, item => [ item.name, item.description ] )
			)
			
			return data
		}
		
		@ $mol_mem
		issues() {
			return this.data_filtered().map( (_,i)=> this.Issue( i ) )
		}
		
		issue_name( index: number ) {
			return this.data_filtered()[ index ].name
		}
		
		@ $mol_mem_key
		issue_date( index: number ) {
			return new $mol_time_moment( this.data_filtered()[ index ].datetime ).toString( 'YYYY-MM-DD' )
		}
		
		issue_type( index: number ) {
			return this.type_name()[ this.data_filtered()[ index ].problem_type ]
		}
		
		issue_uri( index: number ) {
			return this.data_filtered()[ index ].commit_link
		}
		
		issue_descr( index: number ) {
			return this.data_filtered()[ index ].description
		}
		
		download_uri() {
			const csv = $mol_csv_serial( this.data_filtered() )
			return `data:text/csv;charset=utf-8,${ encodeURIComponent( csv ) }`
		}
		
		download_name() {
			return `toxic-repos_${ this.spread() }_${ this.search() }.csv`
		}
		
	}
	
}
